# Hệ thống Quản lý Phiếu Giao Hàng Dự Án Xây Dựng

Hệ thống quản lý phiếu giao nhận vật tư trong các dự án xây dựng, cho phép theo dõi vật tư từ lúc giao đến công trình cho đến khi được xác nhận nhận hàng.

## Cấu trúc dự án

```
construction_delivery_system/
├── models/                  - Thư mục chứa các mô hình dữ liệu Pydantic
│   ├── __init__.py
│   └── delivery_note.py     - Mô hình Pydantic cho phiếu giao hàng
├── repositories/            - Thư mục chứa các lớp repository để tương tác với dữ liệu
│   ├── __init__.py
│   └── delivery_repository.py - Repository cho phiếu giao hàng
├── services/                - Thư mục chứa các lớp service (xử lý logic nghiệp vụ)
│   ├── __init__.py
│   └── delivery_service.py  - Service cho phiếu giao hàng
├── data/                    - Thư mục lưu trữ dữ liệu (sẽ được tạo tự động)
│   └── delivery_notes.json  - File dữ liệu chứa các phiếu giao hàng
├── __init__.py
├── main.py                  - File chính chạy ứng dụng FastAPI
├── init_sample_data.py      - Script tạo dữ liệu mẫu
└── requirements.txt         - Các thư viện cần thiết
```

## Cài đặt

1. Clone dự án:

```bash
git clone <repository-url>
cd construction_delivery_system
```

2. Tạo và kích hoạt môi trường ảo:

```bash
# Tạo môi trường ảo
python -m venv env

# Kích hoạt môi trường ảo (trên Windows)
env\Scripts\activate

# Kích hoạt môi trường ảo (trên Linux/Mac)
source env/bin/activate
```

3. Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

1. Tạo dữ liệu mẫu (tùy chọn):

```bash
python init_sample_data.py
```

2. Chạy ứng dụng:

```bash
python main.py
```

Mặc định, ứng dụng sẽ chạy tại địa chỉ: http://localhost:8000

## API Endpoints

- `GET /` - Trang chủ
- `GET /api/delivery-notes` - Lấy danh sách tất cả phiếu giao hàng
- `GET /api/delivery-notes/{delivery_id}` - Lấy thông tin một phiếu giao hàng cụ thể
- `POST /api/delivery-notes` - Tạo phiếu giao hàng mới
- `PUT /api/delivery-notes/{delivery_id}` - Cập nhật thông tin phiếu giao hàng
- `PATCH /api/delivery-notes/{delivery_id}/status` - Cập nhật trạng thái phiếu giao hàng

## Tài liệu API

Sau khi khởi động ứng dụng, bạn có thể truy cập tài liệu API tại:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Ví dụ về cấu trúc JSON

```json
{
  "delivery_note_id": "GH-CT20240507-001",
  "reference_purchase_order": "PO-20240501-002",
  "delivery_date": "2025-05-07T08:30:00",
  "delivery_status": "delivered",
  "project": {
    "project_id": "DA-CT01",
    "project_name": "Xây dựng Trung tâm Hành chính Q9",
    "site_location": "Đường 123, Phường Phú Hữu, TP. Thủ Đức",
    "contractor_name": "Công ty TNHH Xây dựng ABC"
  },
  "delivery_zone": "Tầng 3 - Khu A",
  "delivered_by": "Nguyễn Văn Tài",
  "vehicle_plate": "51C-123.45",
  "receiver": {
    "receiver_name": "Trần Đức Minh",
    "receiver_role": "Tư vấn giám sát",
    "phone": "0911223344",
    "department": "TVGS Công ty Delta"
  },
  "materials": [
    {
      "material_code": "VT01",
      "name": "Thép phi 16",
      "specification": "CB300-V, dài 11.7m",
      "unit": "Cây",
      "quantity_delivered": 100,
      "quantity_received": 98,
      "remarks": "2 cây cong vênh",
      "batch_number": "BATCH-THP-0425"
    },
    {
      "material_code": "VT02",
      "name": "Xi măng Holcim",
      "specification": "50kg/bao",
      "unit": "Bao",
      "quantity_delivered": 200,
      "quantity_received": 200,
      "remarks": null,
      "batch_number": null
    }
  ],
  "created_at": "2025-05-07T09:00:00",
  "confirmed_at": "2025-05-07T10:00:00",
  "receiver_signature": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  "contractor_signature": "https://example.com/signatures/gh-ct20240507-001/contractor.png",
  "notes": "Giao đúng tiến độ theo yêu cầu",
  "total_quantity": 300
}
``` 