class DailyEmail:

  def send_daily_email(self, msg):
    print('Conneting to smtp...')
    print('Sent message {0} to {1}'.format(msg, self.email))