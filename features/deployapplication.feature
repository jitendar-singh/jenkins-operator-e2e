Feature: Deploy-Application.feature

   Feature Description
    Scenario: Create jenkins application directly
        Given I have a project
        When I run the :new_app client command with:
        | image_stream | openshift/jenkins:2 |
        Then the step should succeed
        And a pod becomes ready with labels:
        | deploymentconfig=jenkins |
        When I execute on the pod:
        |  ls | -la | /usr/bin/java |
        Then the step should succeed
        Then the output should contain:
        | /usr/bin/java -> /etc/alternatives/java |