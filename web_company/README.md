## Docker compose - Scrapy - MongoDB

### Menu
1. [Scrapy](#scrapy)
2. [MongoDB](#mongodb)
3. [Docker](#docker)

### **Scrapy**

#### Sau khi tạo project và spider, các thư mục và file trong thư mục web_company sẽ được tạo tự động (bao gồm thư mục con tên web_company và file scrapy.cfg)

- Dữ liệu cào về được code trong file [web_company/spiders/yellow.py](https://github.com/digitechglobal/Scrapy/blob/docker/web_company/web_company/spiders/yellow.py)
- Tùy chỉnh các thông số về định dạng text, delay_time,.. trong file [web_company/settings.py](https://github.com/digitechglobal/Scrapy/blob/docker/web_company/web_company/settings.py)

### **MongoDB**

- Dữ liệu sau khi được cào về sẽ được lưu trữ vào mongodb (có thể tùy chỉnh ở file [piplines.py](https://github.com/digitechglobal/Scrapy/blob/docker/web_company/web_company/pipelines.py))
- Để truy xuất cơ sở dữ liệu ở trên terminal dùng các câu lệnh:
  - `sudo docker exec -it web_company_mongodb_1 sh` để truy xuất vào container mongodb.
  - `mongo` để truy cập vào mongo shell. (Dùng `db` để test)
  - `use admin` để sử dụng database admin.
  - `db.auth("username", "password")` để xác thực quyền truy cập.
  - `use <db_name>` để vào database được chọn. (`show dbs` để hiển thị danh sách database)
  - `db.<collection_name>.find()` để hiển thị dữ liệu. (`show collections` để hiển thị danh sách collection)
  - `exit` để thoát khỏi mongo shell và cũng câu lệnh đó để thoát khỏi container.
- Dữ liệu trong database được lưu vào thư mục "./data/db".

### **Docker**

#### Các file như: docker-compose.yml, Dockerfile, requirements.txt được tạo để cài đặt cấu hình docker

#### Thư mục Data_crawl được tạo ra để chứa các file trả về sau khi cào thành công

#### Để build docker (cd đến thư mục chứa Dockerfile)
> sudo docker-compose build
#### Để run (cd đến thư mục chứa Dockerfile)
>sudo docker-compose up

#### Giao diện quản lý database
 - File *docker-compose.yml* dùng *mongo-express* để quản lý database với quyền root. 
   * Để sử dụng mongo-express truy cập localhost:8081
 - File *docker-compse-adminer.yml* dùng *adminer* để quản lý database (chỉ cho phép vào database: bar).
   * `sudo docker-compose -f <file-name> up` để run cụ thể trình quản lý database.
   * Để sử dụng adminer truy cập localhost:8080, đăng nhập với username: `root2` password: `1234` server: `mongodb` 
   * Thông tin user được lưu ở file ./mongo1-init.js
