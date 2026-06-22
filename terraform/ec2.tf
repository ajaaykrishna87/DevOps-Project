resource "aws_instance" "terraform_server" {
  ami           = "ami-05bfa4a7765f38076"
  instance_type = "t3.micro"
  key_name      = "test111"

  vpc_security_group_ids = [
    aws_security_group.flask_sg.id
  ]

  user_data = file("${path.module}/user-data.sh")

  tags = {
    Name = "terraform-server"
  }
}
