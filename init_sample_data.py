import os
import json
from datetime import datetime
from models.delivery_note import (
    DeliveryNoteConstruction, 
    ProjectInfo, 
    ReceiverInfo, 
    MaterialItem, 
    DeliveryStatus
)

def create_sample_data():
    """Create sample delivery notes for testing"""
    
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # Sample data file path
    data_file = os.path.join(data_dir, "delivery_notes.json")
    
    # Create sample delivery notes
    sample_notes = [
        # Sample note 1
        DeliveryNoteConstruction(
            delivery_note_id="GH-CT20240507-001",
            reference_purchase_order="PO-20240501-002",
            delivery_date=datetime(2025, 5, 7, 8, 30),
            delivery_status=DeliveryStatus.delivered,
            project=ProjectInfo(
                project_id="DA-CT01",
                project_name="Xây dựng Trung tâm Hành chính Q9",
                site_location="Đường 123, Phường Phú Hữu, TP. Thủ Đức",
                contractor_name="Công ty TNHH Xây dựng ABC"
            ),
            delivery_zone="Tầng 3 - Khu A",
            delivered_by="Nguyễn Văn Tài",
            vehicle_plate="51C-123.45",
            receiver=ReceiverInfo(
                receiver_name="Trần Đức Minh",
                receiver_role="Tư vấn giám sát",
                phone="0911223344",
                department="TVGS Công ty Delta"
            ),
            materials=[
                MaterialItem(
                    material_code="VT01",
                    name="Thép phi 16",
                    specification="CB300-V, dài 11.7m",
                    unit="Cây",
                    quantity_delivered=100,
                    quantity_received=98,
                    remarks="2 cây cong vênh",
                    batch_number="BATCH-THP-0425"
                ),
                MaterialItem(
                    material_code="VT02",
                    name="Xi măng Holcim",
                    specification="50kg/bao",
                    unit="Bao",
                    quantity_delivered=200,
                    quantity_received=200
                )
            ],
            created_at=datetime(2025, 5, 7, 9, 0),
            confirmed_at=datetime(2025, 5, 7, 10, 0),
            receiver_signature="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
            contractor_signature="https://example.com/signatures/gh-ct20240507-001/contractor.png",
            notes="Giao đúng tiến độ theo yêu cầu",
            total_quantity=300
        ),
        
        # Sample note 2
        DeliveryNoteConstruction(
            delivery_note_id="GH-CT20240508-002",
            delivery_date=datetime(2025, 5, 8, 9, 15),
            delivery_status=DeliveryStatus.pending,
            project=ProjectInfo(
                project_id="DA-CT01",
                project_name="Xây dựng Trung tâm Hành chính Q9",
                site_location="Đường 123, Phường Phú Hữu, TP. Thủ Đức",
                contractor_name="Công ty TNHH Xây dựng ABC"
            ),
            delivery_zone="Tầng 4 - Khu B",
            delivered_by="Phạm Văn Bình",
            vehicle_plate="51C-456.78",
            receiver=ReceiverInfo(
                receiver_name="Lê Thanh Hải",
                receiver_role="Chỉ huy trưởng",
                phone="0977889900",
                department="Ban quản lý dự án"
            ),
            materials=[
                MaterialItem(
                    material_code="VT03",
                    name="Gạch ốp lát 60x60",
                    specification="Gạch Granite cao cấp",
                    unit="Thùng",
                    quantity_delivered=50,
                    batch_number="GL-60-2024-0501"
                ),
                MaterialItem(
                    material_code="VT04",
                    name="Keo dán gạch",
                    unit="Bao",
                    quantity_delivered=80
                )
            ],
            created_at=datetime(2025, 5, 8, 8, 30),
            total_quantity=130
        ),
        
        # Sample note 3
        DeliveryNoteConstruction(
            delivery_note_id="GH-CT20240510-003",
            reference_purchase_order="PO-20240505-003",
            delivery_date=datetime(2025, 5, 10, 14, 0),
            delivery_status=DeliveryStatus.partially_delivered,
            project=ProjectInfo(
                project_id="DA-CT02",
                project_name="Khu dân cư Vinhomes",
                site_location="Đường Nguyễn Xiển, Quận 9, TP.HCM",
                contractor_name="Công ty CP Xây dựng XYZ"
            ),
            delivered_by="Trần Văn Cường",
            vehicle_plate="51D-789.12",
            receiver=ReceiverInfo(
                receiver_name="Nguyễn Minh Tuấn",
                receiver_role="Đội trưởng thi công",
                phone="0966778899"
            ),
            materials=[
                MaterialItem(
                    material_code="VT05",
                    name="Ống nước PVC",
                    specification="Phi 90, dài 4m",
                    unit="Cây",
                    quantity_delivered=150,
                    quantity_received=130,
                    remarks="20 cây bị nứt"
                ),
                MaterialItem(
                    material_code="VT06",
                    name="Keo dán ống nước",
                    specification="Lon 250ml",
                    unit="Lon",
                    quantity_delivered=30,
                    quantity_received=30
                )
            ],
            created_at=datetime(2025, 5, 10, 13, 45),
            confirmed_at=datetime(2025, 5, 10, 15, 30),
            notes="Giao thiếu do khó khăn vật tư",
            total_quantity=180
        )
    ]
    
    # Convert to JSON serializable format
    serialized_data = []
    for note in sample_notes:
        note_dict = note.dict()
        # Convert datetime objects to ISO format strings
        for key, value in note_dict.items():
            if isinstance(value, datetime):
                note_dict[key] = value.isoformat()
        serialized_data.append(note_dict)
    
    # Save to file
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(serialized_data, f, ensure_ascii=False, indent=2)
    
    print(f"Created sample data with {len(sample_notes)} delivery notes")

if __name__ == "__main__":
    create_sample_data() 