test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you forgot to return something.
          >>> total_squared_error(0, 0) is not None
          True
          >>> # It looks like you took a square root, but
          >>> # we didn't want you to do that in this exercise.
          >>> np.isclose(15.25**0.5, total_squared_error(0, 0))
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
