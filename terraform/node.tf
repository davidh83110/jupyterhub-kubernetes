data "aws_ami" "eks-worker" {
  filter {
    name   = "name"
    values = ["amazon-eks-node*"]
  }

  filter {
    name   = "description"
    values = ["*1.13*"] # Suggested version from https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html#eks-launch-workers
  }

  most_recent = true
  owners      = ["602401143452"] # Amazon EKS AMI Account ID
}

resource "aws_launch_configuration" "ec2-launch-config" {
  associate_public_ip_address = true
  iam_instance_profile        = "eksInstanceRole"
  image_id                    = "${data.aws_ami.eks-worker.id}"
  instance_type               = "t3.medium"
  name_prefix                 = "david-test - eksNode"
  security_groups             = ["sg-e4343880"]
  user_data_base64            = "${base64encode(data.template_file.ec2-user-data.rendered)}"
  key_name                    = "david-test-key"

  root_block_device {
    volume_size = "100"
  }

  lifecycle {
    create_before_destroy = true
  }
}


resource "aws_autoscaling_group" "ec2-autoscaling" {
  desired_capacity     = 3
  launch_configuration = "${aws_launch_configuration.ec2-launch-config.id}"
  max_size             = 3
  min_size             = 3
  name                 = "david-test-eksNode-autoscaling-group"
  vpc_zone_identifier  = ["subnet-09610138c8417908c, subnet-f18f2987"]

  tag {
    key                 = "Name"
    value               = "david-test - eksNode"
    propagate_at_launch = true
  }

  tag {
    key                 = "kubernetes.io/cluster/david-test"
    value               = "owned"
    propagate_at_launch = true
  }
}
