### Python vs PHP vs Go - Hello world!

Сравним скорость вывода строки «Hello world!» в PHP и Python. Для эталона скорости будем использовать Golang в интерактивном режиме.

# python

```python
print("hello world!")
```
# php
```php
echo "hello world!";
```
# GO
```go
package main
import "fmt"
func main() {
    fmt.Println("hello world!")
}
```

## Результат

![lucky_python](https://github.com/crmscope/lucky_python/blob/main/speed/img/hello_world_result.png)

Как можно заметить на простом выводе строки быстрее всех справился PHP затем Python Затем Golang
