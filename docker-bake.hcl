group "default" {
  targets = ["app-ejemplo"]
}

target "app-ejemplo" {
  context = "."
  dockerfile = "Dockerfile"
  tags = ["lugosnow/app-ejemplo:latest"]
}
