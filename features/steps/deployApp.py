from behave import *
import os

@given(u'I have a project')
def step_impl(context):
    os.system('oc get projects')


@when(u'I run the :new_app client command with')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the :new_app client command with')


@then(u'the step should succeed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the step should succeed')


@then(u'a pod becomes ready with labels')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a pod becomes ready with labels')


@when(u'I execute on the pod')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I execute on the pod')


@then(u'the output should contain')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should contain')