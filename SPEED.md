### Python vs PHP vs Go - Hello world!

Сравним скорость вывода строки «Hello world!» в PHP,  Python и Golang.
Для теста я использую Ubuntu 22.04, go1.23.1, PHP 7.3.33, Python 3.10.6

## Тест Hello world!

### python
```python
print("hello world!")
```
### php
```php
echo "hello world!";
```
### GO
```go
package main
import "fmt"
func main() {
    fmt.Println("hello world!")
}
```

## Результат

![lucky_python](https://github.com/crmscope/lucky_python/blob/main/speed/img/hello_world_result.png)


Результат достаточно предсказуем. Скомпилированный golang файл отработал в десятки раз быстрее нескомпелированных.  Python на 30% быстрее php, а нескомпелированный код Golang показал самый медленный результат.

## Тест цикла на 100 000 итераций с конконтенацией строки.


### python
```python
str = ""
i = 0
while i < 100000 : 
    str += "1"
    i += 1

print(str)
```
### php
```php
$str = "";
for ($i=0; $i < 100000; $i++) {
    $str .= "1";
}
echo $str;
```
### GO
```go
package main
import "fmt"
func main() {
    var str string
    for i := 0; i < 100000; i++{
        str += "1";
    }
    fmt.Println(str)
}
```
## Результат

![lucky_python](https://github.com/crmscope/lucky_python/blob/main/speed/img/cycle_result.png)

Результаты получились крайне не однозначные.  Код golang  как скампилированный так и нет работает примерно с одинаковой скоростью. А PHP и Python отработали на порядок быстрее.