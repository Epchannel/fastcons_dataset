from pydantic import BaseModel, Field, constr
from typing import List, Optional
from datetime import datetime
from enum import Enum


class DeliveryStatus(str, Enum):
    pending = "pending"
    delivering = "delivering"
    delivered = "delivered"
    partially_delivered = "partially_delivered"
    rejected = "rejected"


class ProjectInfo(BaseModel):
    project_id: str = Field(..., description="Mã dự án")
    project_name: str = Field(..., description="Tên dự án")
    site_location: str = Field(..., description="Địa điểm công trình")
    contractor_name: str = Field(..., description="Đơn vị thi công")


class ReceiverInfo(BaseModel):
    receiver_name: str = Field(..., description="Người nhận vật tư")
    receiver_role: str = Field(..., description="Vai trò (Chỉ huy trưởng, Tư vấn giám sát, Đội trưởng thi công...)")
    phone: Optional[constr(min_length=10, max_length=15)] = None
    department: Optional[str] = None


class MaterialItem(BaseModel):
    material_code: str = Field(..., description="Mã vật tư")
    name: str = Field(..., description="Tên vật tư")
    specification: Optional[str] = Field(None, description="Quy cách/Kích thước")
    unit: str = Field(..., description="Đơn vị tính")
    quantity_delivered: float = Field(..., gt=0, description="Số lượng giao")
    quantity_received: Optional[float] = Field(None, description="Số lượng thực nhận")
    remarks: Optional[str] = Field(None, description="Ghi chú (hư hỏng, thiếu, tồn kho...)")
    batch_number: Optional[str] = Field(None, description="Mã lô nếu có")


class DeliveryNoteConstruction(BaseModel):
    delivery_note_id: str = Field(..., description="Số phiếu giao hàng")
    reference_purchase_order: Optional[str] = Field(None, description="Số PO hoặc Đơn đặt hàng liên quan")
    delivery_date: datetime = Field(..., description="Ngày giao vật tư")
    delivery_status: DeliveryStatus = Field(default=DeliveryStatus.pending)

    project: ProjectInfo
    delivery_zone: Optional[str] = Field(None, description="Khu vực giao (Ví dụ: Tầng 5 - Khu A)")
    
    delivered_by: str = Field(..., description="Người giao hàng / Lái xe / Thủ kho")
    vehicle_plate: Optional[str] = Field(None, description="Biển số xe vận chuyển")
    
    receiver: ReceiverInfo
    materials: List[MaterialItem]
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    confirmed_at: Optional[datetime] = Field(None, description="Thời gian xác nhận giao thành công")

    receiver_signature: Optional[str] = Field(None, description="Chữ ký người nhận (base64 hoặc URL)")
    contractor_signature: Optional[str] = Field(None, description="Chữ ký đại diện nhà thầu")
    notes: Optional[str] = Field(None, description="Ghi chú chung")

    total_quantity: Optional[float] = Field(None, description="Tổng số lượng vật tư") 