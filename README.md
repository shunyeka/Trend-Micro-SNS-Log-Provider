# Trend Micro SNS Log Provider

This serverless application integrates with Trend Micro Deep Security which sends an event notification to AWS CloudWatch using SNS and Lambda function.

Made with ❤️ by ShunyEka Systems Pvt.Ltd. Available on the [AWS Serverless Application Repository](https://aws.amazon.com/serverless)

Notification is a key component to provide a security feedback loop to enhance DevSecOps practice. Trend Micro Deep Security has rich APIs that can be used to integrate reporting and notification. We have used the Deep Security Event Forwarding technic which sends a notification to AWS SNS, then this notification delegates to the CloudWatch using lambda function. 

To make it more reliable and easy to deploy we have created an event notification listener as a serverless application that uses AWS SNS, Lambda function, and CloudWatch. We have hosted this application in a serverless application repository for easy single-click deployment for a customer. It is accessible from the public AWS serverless application repository. 
  
After deployment needs to add AWS SNS Topic `ARN` along with Access and Secret Keys into Deep Security inside `Administration>Event Forwarding>Amazon SNS` field, for connecting with Trend Micro Deep Security to AWS SNS.
  
## Steps to configure Trend Micro SNS Log Provider serverless application.
Go to AWS serverless application repository to navigate to the deployment

![search_appication](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/blob/main/images/search_appication.jpg)
   Click on the deploy button to deploy the serverless application.
   
After deployment a new SNS Topic will be created, need to take AWS SNS Topic `ARN` from this newly created SNS Topic, this ARN along with Access and Secret Keys are required for connecting with Trend Micro Deep Security, all those required data are added inside `Administration>Event Forwarding>Amazon SNS` field


![get_arn](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/blob/main/images/get_arn.jpg)

Add SNS Topic `arn` and `keys` into Deep Security inside `Administration>Event Forwarding>Amazon SNS` field

![add_arn](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/blob/main/images/add_arn.jpg)

NOTE: Please Click the `Test credential and send notification` button to verify valid credentials and is it sending notification properly.

Visit the CloudWatch log 

![visit_cloudwatch](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/blob/main/images/visit_cloudwatch.jpg)
 
Now, you can able to see the notification coming from Trend Micro Deep security.

We appreciate your feedback on any enhancement that needs to be done.

## License

Apache License 2.0 (undefined)
