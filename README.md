## Data Specification (for the whole dataset)

### Class Definition (total 95)
| No | Category | Tag field (subclasses) | Description |
|----|----------|------------------------|-------------|
| 1 | document_info (5) | document_info.document_type | tên chính xác của loại tài liệu (phiếu xuất kho, hóa đơn, biên bản...) |
| 2 | | document_info.document_group | nhóm tài liệu (báo giá và đặt hàng, biên bản giao nhận, xuất/nhập kho...) |
| 3 | | document_info.document_number | số chứng từ/phiếu/hóa đơn |
| 4 | | document_info.issue_date | ngày phát hành tài liệu |
| 5 | | document_info.reference_number | số tham chiếu khác trong chứng từ/phiếu/hóa đơn |
| 6 | company_info (7) | company_info.name | tên công ty phát hành chứng từ/phiếu/hóa đơn |
| 7 | | company_info.address | địa chỉ công ty phát hành |
| 8 | | company_info.tax_code | mã số thuế công ty phát hành |
| 9 | | company_info.contact | thông tin liên hệ (điện thoại/email) |
| 10 | | company_info.representative | người đại diện công ty |
| 11 | | company_info.position | chức vụ người đại diện |
| 12 | | company_info.department | phòng ban liên quan |
| 13 | customer_info (6) | customer_info.name | tên khách hàng/bên nhận |
| 14 | | customer_info.address | địa chỉ khách hàng |
| 15 | | customer_info.tax_code | mã số thuế khách hàng |
| 16 | | customer_info.contact | thông tin liên hệ khách hàng |
| 17 | | customer_info.representative | người đại diện khách hàng |
| 18 | | customer_info.position | chức vụ người đại diện khách hàng |
