data "aws_availability_zones" "az" {
  state = "available"
  
}
# output "az" {
#     value = data.aws_availability_zones.az.names
# }
resource "aws_vpc" "pizza_helper_vpc" {
    cidr_block = var.cidr-block
    enable_dns_hostnames = alltrue([true])
    tags = {
        Name = "Pizza-Helper"
    }
  
}
resource "aws_subnet" "public_pizza_helper_subnet-1" {
    vpc_id = aws_vpc.pizza_helper_vpc.id
    map_public_ip_on_launch = true
    cidr_block = cidrsubnet(var.cidr-block, 8, 0)
    availability_zone = data.aws_availability_zones.az.names[0]
    tags = {
        Name = "Public-Pizza-Helper-Subnet-1"
        "kubernetes.io/role/elb" = "1"
        "kubernetes.io/cluster/pizza-helper-cluster" = "shared"
    }
  
}
resource "aws_subnet" "public_pizza_helper_subnet-2" {
    vpc_id = aws_vpc.pizza_helper_vpc.id
    map_public_ip_on_launch = true
    cidr_block = cidrsubnet(var.cidr-block, 8, 2)
    availability_zone = data.aws_availability_zones.az.names[1]
    tags = {
        Name = "Public-Pizza-Helper-Subnet-2"
        "kubernetes.io/role/elb" = "1"
        "kubernetes.io/cluster/pizza-helper-cluster" = "shared"
    }
  
}
resource "aws_subnet" "privete_pizza_helper_subnet-1" {
    vpc_id = aws_vpc.pizza_helper_vpc.id
    cidr_block = cidrsubnet(var.cidr-block, 8, 1)
    availability_zone = data.aws_availability_zones.az.names[0]
    tags = {
        Name = "Private-Pizza-Helper-Subnet-1"
    }
  
}
resource "aws_subnet" "privete_pizza_helper_subnet-2" {
    vpc_id = aws_vpc.pizza_helper_vpc.id
    cidr_block = cidrsubnet(var.cidr-block, 8, 3)
    availability_zone = data.aws_availability_zones.az.names[1]
    tags = {
        Name = "Private-Pizza-Helper-Subnet-2"
    }
  
}
resource "aws_internet_gateway" "pizza_helper_igw" {
    vpc_id = aws_vpc.pizza_helper_vpc.id
    tags = {
        Name = "Pizza-Helper-Internet-Gateway"
    }

}

resource "aws_route_table" "public_route_table" {
    vpc_id = aws_vpc.pizza_helper_vpc.id
    route {
        cidr_block = var.cidr-block
        gateway_id = aws_internet_gateway.pizza_helper_igw.id
    }
    tags = {
        Name = "Public-Route-Table"
    }
  
}
resource "aws_route_table_association" "public_rt_association-1" {
    subnet_id = aws_subnet.public_pizza_helper_subnet-1.id
    route_table_id = aws_route_table.public_route_table.id
  
}
resource "aws_route_table_association" "public_rt_association-2" {
    subnet_id = aws_subnet.public_pizza_helper_subnet-2.id
    route_table_id = aws_route_table.public_route_table.id
}
