output "security_group_id" {
  value = aws_security_group.flask_sg.id
}

output "instance_id" {
  value = aws_instance.terraform_server.id
}

output "public_ip" {
  value = aws_instance.terraform_server.public_ip
}
