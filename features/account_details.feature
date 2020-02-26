Feature: Jenkins-Operator.feature

 Scenario: Starting the jenkins operator
  Given We have a cluster up and running
   When When we run new-app client command
    Then The following resources are created:
        |route.route.openshift.io "jenkins"                   |
        |persistentvolumeclaim "jenkins"                      |
        |deploymentconfig.apps.openshift.io "jenkins"         |
        |serviceaccount "jenkins"                             |
        |rolebinding.authorization.openshift.io "jenkins_edit"|
        |service "jenkins-jnlp"                               |
        |service "jenkins"                                    |
    #  And The route to access the application is generated with output message:
    #     |Success|

    