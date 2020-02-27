
from behave import *
import os

@given(u'I have a jenkins v1 application')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a jenkins v1 application')


@when(u'I give project edit role to the default service account')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I give project edit role to the default service account')


@given(u'a pod becomes ready with labels')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a pod becomes ready with labels')


@then(u'the output should match "^[1-9][0-9]*$"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "^[1-9][0-9]*$"')


@given(u'I have a jenkins browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a jenkins browser')


@given(u'I log in to jenkins')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I log in to jenkins')


@when(u'I perform the :jenkins_trigger_sample_openshift_build web action with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I perform the :jenkins_trigger_sample_openshift_build web action with')


@when(u'I perform the :jenkins_build_now web action with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I perform the :jenkins_build_now web action with')


@given(u'the "frontend-1" build was created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the "frontend-1" build was created')


@given(u'the "frontend-1" build completes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the "frontend-1" build completes')


@given(u'I get project services')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I get project services')


@given(u'I get project deploymentconfigs')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I get project deploymentconfigs')


@given(u'I get project is')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I get project is')


@when(u'I run the :describe client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :describe client command with')


@given(u'the "frontend-2" build was created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the "frontend-2" build was created')


@given(u'the "frontend-2" build completes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the "frontend-2" build completes')


@given(u'I have a jenkins v2 application')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a jenkins v2 application')


@given(u'the "jenkins" PVC becomes :bound within 300 seconds')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the "jenkins" PVC becomes :bound within 300 seconds')


@then(u'the expression should be true> Integer(@result[:response]) > 0')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the expression should be true> Integer(@result[:response]) > 0')


@when(u'I run the :start_build client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :start_build client command with')


@given(u'the "openshift-jee-sample-1" build completes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the "openshift-jee-sample-1" build completes')


@when(u'I run the :policy_add_role_to_user client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :policy_add_role_to_user client command with')


@when(u'I perform the :jenkins_create_pipeline_job web action with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I perform the :jenkins_create_pipeline_job web action with')


@given(u'I download a file from "https://raw.githubusercontent.com/openshift-qe/v3-testfiles/master/templates/OCP_12075/pipeline_delete_resource.groovy"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I download a file from "https://raw.githubusercontent.com/openshift-qe/v3-testfiles/master/templates/OCP_12075/pipeline_delete_resource.groovy"')


@given(u'I replace lines in "pipeline_delete_resource.groovy"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I replace lines in "pipeline_delete_resource.groovy"')


@when(u'I perform the :jenkins_pipeline_insert_script web action with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I perform the :jenkins_pipeline_insert_script web action with')


@when(u'I perform the :jenkins_verify_job_success web action with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I perform the :jenkins_verify_job_success web action with')


@given(u'I get project dc named "frontend"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I get project dc named "frontend"')


@then(u'the output should contain "not found"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should contain "not found"')


@given(u'I get project builds')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I get project builds')


@then(u'the output should contain "No resources found"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should contain "No resources found"')


@then(u'the output should not match "origin-nodejs-sample\s+latest"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should not match "origin-nodejs-sample\s+latest"')


@when(u'I run the :get client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :get client command with')


@then(u'the output should match "nodejs-ex-pipeline.*JenkinsPipeline"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "nodejs-ex-pipeline.*JenkinsPipeline"')


@when(u'I run the :delete client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :delete client command with')


@then(u'the output should match "nodejs-ex-pipeline1.*JenkinsPipeline"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "nodejs-ex-pipeline1.*JenkinsPipeline"')


@then(u'the output should match "nodejs-ex-pipeline2.*JenkinsPipeline"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "nodejs-ex-pipeline2.*JenkinsPipeline"')


@then(u'the output should match "nodejs-ex-pipeline3.*JenkinsPipeline"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "nodejs-ex-pipeline3.*JenkinsPipeline"')


@when(u'I run the :new_build client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :new_build client command with')


@then(u'the output should match "nodejs-ex-pipeline4.*JenkinsPipeline"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "nodejs-ex-pipeline4.*JenkinsPipeline"')


@then(u'the output should match "nodejs-ex-pipeline5.*JenkinsPipeline"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "nodejs-ex-pipeline5.*JenkinsPipeline"')


@then(u'the output should match "nodejs-ex-pipeline6.*JenkinsPipeline"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "nodejs-ex-pipeline6.*JenkinsPipeline"')


@then(u'the output should match "nodejs-ex-pipeline7.*JenkinsPipeline"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should match "nodejs-ex-pipeline7.*JenkinsPipeline"')


@then(u'the "sample-pipeline-1" build completes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "sample-pipeline-1" build completes')


@when(u'I perform the :goto_jenkins_buildlog_page web action with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I perform the :goto_jenkins_buildlog_page web action with')


@when(u'I get the visible text on web html page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I get the visible text on web html page')


@when(u'I run the :patch client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :patch client command with')


@when(u'I perform the :jenkins_check_build_string_parameter web action with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I perform the :jenkins_check_build_string_parameter web action with')


@then(u'the "sample-pipeline-2" build completes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "sample-pipeline-2" build completes')


@then(u'the step should fail')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the step should fail')


@then(u'I have a project')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I have a project')


@when(u'I run the :create client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :create client command with')


@then(u'evaluation of `pod.name` is stored in the :jenkins_pod clipboard')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then evaluation of `pod.name` is stored in the :jenkins_pod clipboard')


@then(u'I run the :start_build client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I run the :start_build client command with')


@when(u'the "sample-pipeline-openshift-client-plugin-1" build becomes :running')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the "sample-pipeline-openshift-client-plugin-1" build becomes :running')


@when(u'the "ruby-1" build becomes :running')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the "ruby-1" build becomes :running')


@then(u'the "ruby-1" build completed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "ruby-1" build completed')


@then(u'the "sample-pipeline-openshift-client-plugin-1" build completed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "sample-pipeline-openshift-client-plugin-1" build completed')


@when(u'I execute on the "<%= cb.jenkins_pod %>" pod')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I execute on the "<%= cb.jenkins_pod %>" pod')


@when(u'I run the :set_env client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :set_env client command with')


@then(u'the project is deleted')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the project is deleted')


@when(u'we run \'oc new new-project jenkins-test\' on the terminal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we run \'oc new new-project jenkins-test\' on the terminal')


@when(u'we run \'oc new-app jenkins-persistent\' on the terminal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we run \'oc new-app jenkins-persistent\' on the terminal')

















































# @given(u'We have a cluster up and running')
# def runOperator(context):
#     print('Jenkins opeartor is running')
#     os.system('oc new-project jenkins-test-5')
    
# @when(u'When we run new-app client command')
# def step_impl(context):
#     os.system('oc new-app jenkins-persistent')


# @then(u'The following resources are created')
# def step_impl(context):
#     os.system('oc get all')
#     print('Resources created succesfully\n')
#     print('Jenkins Operator is running')
#     print('Lets commit')