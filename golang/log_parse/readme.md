
```
▶ go mod init log_parse
go: creating new go.mod: module log_parse
```

生成解析go源码
```
▶ ldetool generate nginx.lde --package main
```

生成一个 nginx_lde.go的文件


具体的测试用例请看 main.go

```
▶ time go run main.go nginx_lde.go
total:  96130191409
go run main.go nginx_lde.go  1.81s user 0.24s system 107% cpu 1.911 total
```
