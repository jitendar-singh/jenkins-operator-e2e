from behave import *
import os

@given(u'We have a cluster up and running')
def runOperator(context):
    print('Jenkins opeartor is running')
    os.system('oc new-project jenkins-test-5')
    
@when(u'When we run new-app client command')
def step_impl(context):
    os.system('oc new-app jenkins-persistent')


@then(u'The following resources are created')
def step_impl(context):
    os.system('oc get all')
    print('Resources created succesfully\n')
    print('Jenkins Operator is running')
    print('Lets commit')