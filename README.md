# Trend Micro Logs CloudWatch Connector

This serverless application integrates with different services of Trend Micro which sends an event notification to AWS CloudWatch using AWS SNS, API Gateway, and Lambda function.

Made with ❤️ by ShunyEka Systems Pvt.Ltd. Available on the [AWS Serverless Application Repository](https://aws.amazon.com/serverless)

Notification is a key component to provide a security feedback loop to enhance DevSecOps practice. Trend Micro Deep Security has rich APIs that can be used to integrate reporting and notification. We have used the Deep Security Event Forwarding technic which sends a notification to AWS SNS, then this notification delegates to the CloudWatch using lambda function. 

To make it more reliable and easy to deploy we have created an event notification listener as a serverless application that uses AWS SNS, API Gateway, Lambda function, and CloudWatch. We have hosted this application in a serverless application repository for easy single-click deployment for a customer. It is accessible from the public AWS serverless application repository. 
      
## Steps to configure Trend Micro Logs CloudWatch Connector serverless application.
Go to AWS serverless application repository to navigate to the deployment

![search_appication](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/raw/main/images/search_appication.jpg)
   Click on the deploy button to deploy the serverless application.

Trend Micro Provide Different Services which are:
1. [Workload Security](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/blob/main/README.md#1-workload-security)
2. [Application Security](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/blob/main/README.md#2-application-security)
3. [Cloud Conformity](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/blob/main/README.md#3-cloud-conformity)
4. [Deep Security Smart Check](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/blob/main/README.md#4-deep-security-smart-check)

Based on Sevice need to do some configuration.

## 1. Workload Security

After deployment a new SNS Topic will be created, need to take AWS SNS Topic `ARN` from this newly created SNS Topic, this ARN along with Access and Secret Keys are required for connecting with Trend Micro Deep Security, we can get or create keys from `IAM User`, all those required data are added inside `Administration>Event Forwarding>Amazon SNS` field

![get_arn](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/raw/main/images/get_arn.jpg)

Add SNS Topic `arn` and `keys` into Deep Security inside `Administration>Event Forwarding>Amazon SNS` field

![add_arn](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/raw/main/images/add_arn.jpg)

NOTE: Please Click the `Test credential and send notification` button to verify valid credentials and is it sending notification properly.

Visit the CloudWatch log 

![visit_cloudwatch](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/raw/main/images/visit_cloudwatch.jpg)

## 2. Application Security
After deployment need to do some configuration in following steps:

1. In the Application Security dashboard, go to `Integrations > Add Integration > Amazon SNS`. Copy the `External ID` to your clipboard. This ID will be used in step six.

2. Go to your AWS console and navigate to the `Identity and Access Management (IAM)` page.
3. Under `Access managemen`t, select `Roles`.
4. Select `Create role`, then `Another AWS` account.
5. In `Account ID`, enter: `800880067056`.
6. Select `Require external ID (Best practice when a third party will assume this role)` and paste the ID that you copied above. Make sure you leave `Require MFA` disabled. Click `Next: Permissions` when you're finished.
7. Select `Create Policy`. A new window opens.
8. You can set up a policy through the `Visual Editor` or `JSON`
   - To create a policy through the `Visual Editor`:
   
     a. In `Choose a Service`, select `SNS`.
     
     b. Under `Access Level`, open the `Write` section and select `Publish`.
     
     c.Under `Resources`, select `All resources`.
    
   - To create a policy through the `JSON` enter the following:
     
         {
            "Version": "2012-10-17",
            "Statement": [
              {
                "Effect": "Allow",
                "Action": "sns:Publish",
                 "Resource": "*"
              }
            ]
         }
           
9. Click `Review Policy`.
10. Enter a name for the policy, for example CloudOneAppSecAWSIntegrationPolicy and provide a description. Click `Create Policy` when you're ready.
11. Navigate back to the `Create role` window and refresh the page. Select the policy you created.
12. Click through `Next: Tags` and `Next: Review`.
13. Give the role a name (you can use the same name as your policy) and a description, and click `Create role`. 

#### Integrate with Application Security
1. Navigate to your Application Security dashboard. In the left menu, select `Integrations`.
2. Click `Add Integration` from the top-right corner.
3. Select `Amazon SNS` from the pop-up window.
4. In the `Configure SNS Integration` window, fill-in the following fields:
- `Account ID`: Your personal account ID.
- `Role Name`: The name of the role you created.
- `External ID`: The external ID that you used when creating you role.
- `Key Hint`: A hint you can use to help you remember what External ID was used to integrate Application Security with Amazon SNS.
- `Region`: The region your AWS account is located. This can be found in the top-right corner of your AWS console.
- `Topic Name`: Name of your topic. For more information, see Create a topic.
- `Notification Format`: Format of the payload sent when there is an alert. The options currently supported are Text or Json, with the default value being Text.
- `Minimum Reported Severity`: The minimum severity of alerts that you'd like to be posted to your slack channel. You can choose between low, medium or high.   

After above configuration need to add any sample file with valunarable script for testing.

Visit the CloudWatch log 

![visit_cloudwatch](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/raw/main/images/visit_cloudwatch.jpg)

## 3. Cloud Conformity
After deployment need to do some configuration in following steps:

1. In the Cloud Conformity dashboard, go to `Dashboard > Select {Account} > Settings > Communication settings > Update communication settings > Configure ‘Amazon SNS’`. 
2. Click on `Create an Amazon SNS channel`
3. Set automatic notifications:
   By default, Automatic Notifications are set to `OFF` for all communication channels. If you want to receive notifications after the Conformity Bot runs, set automatic notifications to `ON`.
4. Set manual notifications:
   The following channels have a manual notifications option

   - Jira Communication
   - Zendesk Communication
   - ServiceNow ITSM Communication
   - Amazon SNS Communication
   
   By default, manual notifications are set to `OFF` for these channels.
   
   If manual notifications is turned `ON`, you can send notifications for failures by navigating to specific rules on the Account dashboard.
   
5. Input `Channel Name` to distinguish the channel from others of the same type.
   Note: The field is limited to 20 characters
   
6. Configure Triggers
7. `Configure now` requires a two-step process
   - Input `SNS Topic ARN`
   - Follow the instructions of `Setup access`

#### Send notification to
##### SNS Topic ARN
```arn:aws:sns:REGION:ACCOUNT_ID:TOPIC_NAME```    

##### Setup access
1. Go to `Key Management Service (KMS)` in the AWS Console.

   - Note: If you already have a key please update your policy to allow key usage permission for AWS account: `717210094962`, then proceed to step 8

2. Click `Customer managed keys` and then `Create key`

3. Use the following details for `Step 1: Add alias and description`. Then click `Next`

   - Alias: `CloudConformitySNSEncryptionKey`
    
   - Description: `CloudConformitySNSEncryptionKey`

4. On `Step 2: Add tags`. Add in tags. Then click Next

5. On `Step 3: Define key administrative permissions`. Select a Key administrator. Then `click Next`

6. On `Step 4: Define key usage permissions`

   - Click `Add another AWS account`, enter `717210094962`
   
   - Click `Next`.

7. On `Step 5: Review and edit key policy`. Review the policy. Click `Finish`

8. If you haven't already done so, create an `SNS Topic` (Simple Notification Service section in the AWS Console)
   
   - Topic Name: `CloudConformity`

9. Select your `SNS topic`, then click `Edit`

10. Expand Encryption section, select Enable encryption.
Under Customer master key (CMK), clear the default aws key and select CloudConformitySNSEncryptionKey

11. Expand Access policy. Update the following code and then add it as a new statement.
`{ "Sid": "a unique statement ID", "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::717210094962:root" }, "Action": "SNS:Publish", "Resource": "Your SNS Topic ARN" }`
Click `Save changes`

12. Enter the SNS Topic's ARN in the field at the top of this window

13. Finally, click `Save` at the bottom of this window


Visit the CloudWatch log 

![visit_cloudwatch](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/raw/main/images/visit_cloudwatch.jpg)


## 4. Deep Security Smart Check

After deployment it will generate API gateway URL that need to be added to DS smart check web console. To add api gateway URL navigate to web hooks in DSSC console and create web hook and add URL.

![get_endpoint](https://github.com/shunyeka/Trend-Micro-Smartcheck-and-Threadfix-serverless-connector/raw/main/images/get_endpoint.jpg)

Once application is deployed add or update bellow environment variables from lambda function.

    Environment Variables:
        DSSC_URL                          <add_smartcheck_url>
        DSSC_SMARTCHECK_USER              <add_smartcheck_user>
        DSSC_SMARTCHECK_PASSWORD          <add_smartcheck_password>
        DSSC_MIN_SEVERITY                 <min_severity>
        DSSC_SHOW_FIXED                   <add_true_or_false>
        DSSC_SHOW_OVERRIDDEN              <add_true_or_false>
        DSSC_INSECURE_SKIP_TLS_VERIFY     <add_true_or_false>




![add_environment](https://github.com/shunyeka/Trend-Micro-Smartcheck-and-Threadfix-serverless-connector/raw/main/images/add_environment.jpg)

Add api gateway URL to DSSC web hook console

![add_api_to_webhook](https://github.com/shunyeka/Trend-Micro-Smartcheck-and-Threadfix-serverless-connector/raw/main/images/add_api_to_webhook.jpg)

Visit the CloudWatch log 

![visit_cloudwatch](https://github.com/shunyeka/Trend-Micro-SNS-Log-Provider/raw/main/images/visit_cloudwatch.jpg)
 
Now, you can able to see the notification coming from Trend Micro Deep security.

We appreciate your feedback on any enhancement that needs to be done.

## License

Apache License 2.0 (undefined)
