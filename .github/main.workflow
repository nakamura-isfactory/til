workflow "Slack Notification Demo" {
  resolves = ["Slack Notification"]
  on = "push"
}

action "Slack Notification" {
  uses = "rtCamp/action-slack-notify@master"
  secrets = ["SLACK_WEBHOOK"]
}