package main
import "fmt"
func main() {
    var str string
    for i := 0; i < 100000; i++{
        str += "1";
    }
    fmt.Println(str)
}