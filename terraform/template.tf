data "template_file" "ec2-user-data" {
  template = "${file("${path.module}/scripts/user_data.tpl")}"

  vars = {
    eks_cluster_endpoint = "${var.eks_cluster_endpoint}"
    eks_cluster_ca       = "${var.eks_cluster_ca}"
    eks_cluster_name     = "david-test"
  }
}

