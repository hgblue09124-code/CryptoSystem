CryptoSystem Development Guide

Quy trình phát triển

Mỗi tính năng mới nên đi qua các bước:

Idea
 ↓
Research
 ↓
Prototype
 ↓
Testing
 ↓
Integration

Không đưa code trực tiếp vào hệ thống chính khi chưa kiểm chứng.

⸻

Quy chuẩn Code

Naming

Sử dụng tiếng Anh:

Đúng:

class DecisionEngine:

Không dùng:

class BoQuyetDinh:

⸻

Module Design

Mỗi module nên có một nhiệm vụ rõ ràng.

Ví dụ:

Không:

trading.py

chứa mọi thứ.

Nên:

collector/
strategy/
risk/
execution/
journal/

⸻

Testing

Trước khi thêm tính năng:

* Kiểm tra dữ liệu đầu vào
* Kiểm tra trường hợp lỗi
* Kiểm tra ảnh hưởng module khác

⸻

Git Workflow

Mỗi thay đổi nên có commit rõ ràng:

Ví dụ:

fix: repair package initialization
feat: add market collector
docs: update Vietnamese documentation

⸻

Mục tiêu

CryptoSystem không chỉ là một bot giao dịch.

Nó là một hệ thống học tập và nghiên cứu:

* hiểu thị trường
* hiểu chiến lược
* hiểu rủi ro
* cải thiện quyết định theo thời gian