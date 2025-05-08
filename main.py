from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import datetime
import os

from models.delivery_note import DeliveryNoteConstruction, DeliveryStatus
from repositories.delivery_repository import DeliveryRepository
from services.delivery_service import DeliveryService

app = FastAPI(
    title="Hệ thống quản lý giao nhận vật tư xây dựng",
    description="API backend cho ứng dụng quản lý phiếu giao hàng trong dự án xây dựng",
    version="0.1.0"
)

# CORS middleware setup for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency injection
def get_delivery_service():
    repo = DeliveryRepository("data/delivery_notes.json")
    return DeliveryService(repo)

@app.get("/")
def read_root():
    return {"message": "Hệ thống quản lý giao nhận vật tư xây dựng"}

@app.get("/api/delivery-notes", response_model=list[DeliveryNoteConstruction])
def get_all_delivery_notes(service: DeliveryService = Depends(get_delivery_service)):
    return service.get_all_delivery_notes()

@app.get("/api/delivery-notes/{delivery_id}", response_model=DeliveryNoteConstruction)
def get_delivery_note(delivery_id: str, service: DeliveryService = Depends(get_delivery_service)):
    note = service.get_delivery_note_by_id(delivery_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy phiếu giao hàng")
    return note

@app.post("/api/delivery-notes", response_model=DeliveryNoteConstruction)
def create_delivery_note(note: DeliveryNoteConstruction, service: DeliveryService = Depends(get_delivery_service)):
    return service.create_delivery_note(note)

@app.put("/api/delivery-notes/{delivery_id}", response_model=DeliveryNoteConstruction)
def update_delivery_note(delivery_id: str, note: DeliveryNoteConstruction, service: DeliveryService = Depends(get_delivery_service)):
    updated_note = service.update_delivery_note(delivery_id, note)
    if updated_note is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy phiếu giao hàng")
    return updated_note

@app.patch("/api/delivery-notes/{delivery_id}/status")
def update_delivery_status(delivery_id: str, status: DeliveryStatus, service: DeliveryService = Depends(get_delivery_service)):
    success = service.update_delivery_status(delivery_id, status)
    if not success:
        raise HTTPException(status_code=404, detail="Không tìm thấy phiếu giao hàng")
    return {"message": f"Đã cập nhật trạng thái thành {status}"}

if __name__ == "__main__":
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Run the FastAPI app with uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 