# Trend Micro SNS Log Provider

This serverless application integrates with Trend Micro Deep Security which sends an event notification to AWS CloudWatch using SNS and Lambda function.

Made with ❤️ by ShunyEka Systems Pvt.Ltd. Available on the [AWS Serverless Application Repository](https://aws.amazon.com/serverless)

Notification is a key component to provide a security feedback loop to enhance DevSecOps practice. Trend Micro Deep Security has rich APIs that can be used to integrate reporting and notification. We have used the Deep Security Event Forwarding technic which sends a notification to AWS SNS, then this notification delegates to the CloudWatch using lambda function. 

To make it more reliable and easy to deploy we have created an event notification listener as a serverless application that uses AWS SNS, Lambda function, and CloudWatch. We have hosted this application in a serverless application repository for easy single-click deployment for a customer. It is accessible from the public AWS serverless application repository. 
  
After deployment a new SNS Topic will be created, need to take AWS SNS Topic `ARN` from this newly created SNS Topic, this ARN along with Access and Secret Keys are required for connecting with Trend Micro Deep Security, all those required data are added inside `Administration>Event Forwarding>Amazon SNS` field 

NOTE: Please Click the `Test credential and send notification` button to verify valid credentials and is it sending notification properly. 
  
## Steps to configure Trend Micro SNS Log Provider serverless application.
Go to AWS serverless application repository to navigate to the deployment

## License

Apache License 2.0 (undefined)
