# standard library
import datetime
import json
import random
import string
import tempfile
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Parse the incoming SNS notification for a Deep Security event
    """
    timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    
    if type(event) == type({}):
        if 'Records' in event:
            print("Processing {} records".format(len(event['Records'])))
            for i, record in enumerate(event['Records']):
                print("Record {}/{}".format(i, len(event['Records'])))

                if 'Sns' in record:
                    timestamp = datetime.datetime.now()
                    time_received = record['Sns']['Timestamp'] if 'Timestamp' in  record['Sns'] else None
                    if time_received: 
                        try:
                            timestamp = datetime.datetime.strptime(time_received, timestamp_format)
                        except: pass # we can silently fail and try to catch later

                    if 'Message' in record['Sns']:
                        record_docs = json.loads(record['Sns']['Message'])

                        # some versions of this feature send single events instead of an array
                        if type(record_docs) == type({}): record_docs = [record_docs]

                        for record_doc in record_docs:
                            if 'LogDate' in record_doc:
                                # LogDate is the actually timestamp of the event. We need a timestamp for the
                                # event and the order of preference is:
                                #    1. LogDate
                                #    2. Time received by Amazon SNS
                                #    3. Time processed by AWS Lambda
                                #
                                # When both LogDate and time received by Amazon SNS are present, we'll also
                                # calculate the delivery delay and record that with the event as 'DeliveryDelay'
                                time_generated = record_doc['LogDate']
                                try:
                                    tg = datetime.datetime.strptime(time_generated, timestamp_format)
                                    timestamp = tg # update the timestamp to the actual event time instead of the time is was received
                                    tr = datetime.datetime.strptime(time_received, timestamp_format)
                                    d = tr - tg
                                    record_doc['DeliveryDelay'] = '{}'.format(d)
                                    logger.info('#####')
                                    logger.info(record_doc)
                                    logger.info('#####')
                                except Exception as err:
                                    print(err)
    else:
        # in case of failure, simply output the log to CloudWatch Logs
        print("Received event: " + json.dumps(event, indent=2))
        
    return True

    
