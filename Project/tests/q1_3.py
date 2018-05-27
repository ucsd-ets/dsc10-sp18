test = {
  'name': '1.3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> f = distance_from("In Your Eyes", "like", "love")
          >>> 0 < f("Insane In The Brain") < 1
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
