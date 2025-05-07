## Data Specification (for the whole dataset)

### Class Definition (total 95)
| No | Category | Tag field (subclasses) | Description |
|----|----------|------------------------|-------------|
| 1 | document_info (5) | document_info.document_type | tên chính xác của loại tài liệu (phiếu xuất kho, hóa đơn, biên bản...) |
| 2 | | document_info.document_group | nhóm tài liệu (báo giá và đặt hàng, biên bản giao nhận, xuất/nhập kho...) |
| 3 | | document_info.document_number | số chứng từ/phiếu/hóa đơn |
| 4 | | document_info.issue_date | ngày phát hành tài liệu |
| 5 | | document_info.reference_number | số tham chiếu khác trong tài liệu |
| 6 | company_info (7) | company_info.name | tên công ty phát hành tài liệu |
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
| 19 | quote_details (6) | quote_details.quote_number | số báo giá |
| 20 | | quote_details.valid_until | thời hạn báo giá |
| 21 | | quote_details.payment_terms | điều khoản thanh toán |
| 22 | | quote_details.delivery_terms | điều khoản giao hàng |
| 23 | | quote_details.warranty_terms | điều khoản bảo hành |
| 24 | | quote_details.project_name | tên dự án/công trình |
| 25 | delivery_details (7) | delivery_details.delivery_address | địa điểm giao hàng |
| 26 | | delivery_details.delivery_time | thời gian giao hàng |
| 27 | | delivery_details.vehicle_info | thông tin phương tiện vận chuyển (biển số xe) |
| 28 | | delivery_details.driver_name | tên người vận chuyển/lái xe |
| 29 | | delivery_details.receiver_position | chức vụ người nhận |
| 30 | | delivery_details.delivery_status | trạng thái giao hàng |
| 31 | | delivery_details.inspection_result | kết quả kiểm tra |
| 32 | warehouse_details (6) | warehouse_details.warehouse_name | tên kho |
| 33 | | warehouse_details.warehouse_keeper | thủ kho |
| 34 | | warehouse_details.reason | lý do xuất/nhập kho |
| 35 | | warehouse_details.destination | nơi nhận hàng |
| 36 | | warehouse_details.source | nguồn hàng |
| 37 | | warehouse_details.stock_balance | tồn kho sau xuất/nhập |
| 38 | payment_details (7) | payment_details.payment_method | phương thức thanh toán |
| 39 | | payment_details.account_number | số tài khoản |
| 40 | | payment_details.bank_name | tên ngân hàng |
| 41 | | payment_details.paid_amount | số tiền đã thanh toán |
| 42 | | payment_details.remaining_balance | số tiền còn lại |
| 43 | | payment_details.due_date | hạn thanh toán |
| 44 | | payment_details.reference_document | chứng từ liên quan |
| 45 | concrete_details (10) | concrete_details.concrete_grade | mác bê tông |
| 46 | | concrete_details.concrete_type | loại bê tông |
| 47 | | concrete_details.construction_site | công trình/địa điểm đổ |
| 48 | | concrete_details.pump_details | thông tin bơm |
| 49 | | concrete_details.vehicle_weight | trọng lượng xe |
| 50 | | concrete_details.mixing_ratio | tỷ lệ trộn |
| 51 | | concrete_details.slump_test | kết quả thử độ sụt |
| 52 | | concrete_details.volume_ordered | khối lượng đặt hàng |
| 53 | | concrete_details.volume_delivered | khối lượng thực tế giao |
| 54 | | concrete_details.temperature | nhiệt độ bê tông |
| 55 | items (13) | items.stt | số thứ tự |
| 56 | | items.item_type | loại (vật tư/dịch vụ/hàng hóa) |
| 57 | | items.product_code | mã sản phẩm/vật tư/dịch vụ |
| 58 | | items.product_name | tên sản phẩm/vật tư/dịch vụ |
| 59 | | items.specification | quy cách/mô tả chi tiết |
| 60 | | items.unit | đơn vị tính |
| 61 | | items.quantity | số lượng |
| 62 | | items.unit_price | đơn giá |
| 63 | | items.total_price | thành tiền |
| 64 | | items.mass | khối lượng (nếu khác với số lượng) |
| 65 | | items.volume | thể tích (nếu áp dụng) |
| 66 | | items.dimension | kích thước (nếu áp dụng) |
| 67 | | items.remarks | ghi chú |
| 68 | sub_total (7) | sub_total.subtotal | tổng tiền hàng chưa thuế |
| 69 | | sub_total.discount_rate | tỷ lệ chiết khấu (%) |
| 70 | | sub_total.discount_amount | số tiền chiết khấu |
| 71 | | sub_total.service_price | phí dịch vụ |
| 72 | | sub_total.other_fees | phí khác |
| 73 | | sub_total.total_weight | tổng khối lượng |
| 74 | | sub_total.total_volume | tổng thể tích |
| 75 | tax (4) | tax.vat_rate | tỷ lệ thuế VAT (%) |
| 76 | | tax.vat_amount | tiền thuế VAT |
| 77 | | tax.withholding_tax | thuế khấu trừ tại nguồn (nếu có) |
| 78 | | tax.other_tax | các loại thuế khác |
| 79 | total (8) | total.grand_total | tổng cộng tiền thanh toán |
| 80 | | total.total_in_words | số tiền bằng chữ |
| 81 | | total.currency | đơn vị tiền tệ |
| 82 | | total.cash_amount | số tiền thanh toán bằng tiền mặt |
| 83 | | total.transfer_amount | số tiền thanh toán bằng chuyển khoản |
| 84 | | total.credit_amount | số tiền thanh toán bằng tín dụng |
| 85 | | total.deposit_amount | số tiền đặt cọc |
| 86 | | total.remaining_amount | số tiền còn lại phải thanh toán |
| 87 | approval (9) | approval.created_by | người lập phiếu |
| 88 | | approval.approved_by | người phê duyệt |
| 89 | | approval.received_by | người nhận |
| 90 | | approval.reviewed_by | người kiểm tra |
| 91 | | approval.created_at | thời gian lập phiếu |
| 92 | | approval.confirmed_at | thời gian xác nhận |
| 93 | | approval.approval_status | trạng thái phê duyệt |
| 94 | | approval.notes | ghi chú bổ sung |
| 95 | | approval.terms_and_conditions | điều khoản và điều kiện |
