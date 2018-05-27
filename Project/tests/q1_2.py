test = {
  'name': '1.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you can use any two songs
          >>> 0 < distance_two_features("Lookin' for Love", "Insane In The Brain", "like", "love") < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you can use any two features
          >>> 0 < distance_two_features("In Your Eyes", "Sangria Wine", "the", "of") < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': r"""
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
