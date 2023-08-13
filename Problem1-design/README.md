# 1. DESIGN
In this section, I will design the system using AWS services with 3-tiers and a caching layer between backend and database for improving performance:
- Front-end layer: interactive with user
- Back-end layer: processing business logic
- Database layer: Storing user data 
- Caching layer: caching data query from database

![image](https://user-images.githubusercontent.com/28616641/260221508-5fca2a9b-9f58-4313-afe3-83b6516812d0.png)

## 1.1 Overview infrastructure
### 1.1.1 Components
- For high availability, the system and all its application will sit in 2 AZs and in each AZ will have 1 public, 1 private subnet, 2 bastion host, 2 NAT gateway.

- For CICD, I use Github Action and CodePipline

- Beside, I also use other common AWS services:
  + Route 53: Redirect domain to cloudfront
  + WAF: Limit access and filter malicious traffic
  + ACM: Provision, manage, and deploy certificates.
  + Cloudfront: Content delivery network (CDN) service for increasing speed the static and dynamic content.
  + EKS: Managed Kubernetes service to run Kubernetes in the AWS
  + GuarDuty:  Threat detection service that continuously monitors for malicious activity and unauthorized behavior.
  + Cloudtrail: Monitors and records account activity 
  + S3: object file storage and will set with life cycle policy: after 30 days move to S3 Intelligent-Tiering and 90 days move to S3 Glacier 
        And after 180 days will move to S3 Glacier Deep Archive
  + KMS: for envelop encryption S3 object and EKS secret.

### 1.1.2 Data workflow
- When users access to domain, Route53 will redirect the traffic to Cloudfront which put the WAF rules.
On these WAF rules, we will set for limiting the IP, regrex pattern, number requests,...
- After passing these rules, the traffic will continue going to ELB. Security group will be applied here for limiting which IP and port can access.
In the case denying specific IP, we can use NACLS.
- Then the traffic will continue go to target group which integrated service by EKS cluster.
- At the EKS cluster level, the traffic after goes through front end and will connects to backend.
  The backend first will check data in Redis. It not exists, it will get data from the database. 

### 1.1.3 CICD workflow
- I use Github action and CodePipeline for CICD
- When a developer push and create new pull request, it will trigger Github action and push manifest to S3 bucket.
- New event in S3 will trigger the CodePipeline and after that, it will be built and deploys application on EKS cluster.

### 1.1.4 Logging and monitoring
- Logs(system, EKS, application) will be stored in S3 and filter by Cloudwatch to trigger and then send alert to monitoring system.
- Besides, we can use third parties monitoring solution such as Datadog, NewRelic,...


## 1.2 Security
- Limiting IP and filter vulnerability traffic by WAF, security group and NACLs.
- IAM role for technicians when accessing services in private subnets.
- Using KMS for encryption objects in S3, secret in EKS.
- Using GuarDuty for threat detection service that continuously monitors for malicious activity and unauthorized behavior.
- Cloudtrail for Monitoring and recording account activity for auditing.

## 1.3 Performance
- Cloudfront for caching static and dynamic content
- Elastic cache for caching database queries

## 1.4 High availability and Scalability 
- I will apply scalability and high availability for these components:
  + Bastion host: Set Route 53 failover policy and autoscaling group.
  + EKS: Autoscaling group for node group and HPA for pod.
  + Redis cluster: Application Auto Scaling to increase or decrease the desired shards or replicas automatically.
  + RDS cluster: Horizontal scaling increases performance by extending the database operations to additional nodes.

## 1.5 Backup and replica
- I will use AWS Backup service for backup important data such as: database, EC2, S3,...
This will replica to another account in other region for HA.

## 1.6 Cost saving
- Apply lifecyle policy for S3 bucket
- Apply snapshot policy for database, EBS storage
- Apply for spot instance type for EKS, EC2
- Apply retention setting for cloudwatch log
- Also, create alert to notify when budget is over threshold

