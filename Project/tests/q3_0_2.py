test = {
  'name': '3.0.2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> set(words.labels) == {'Word', 'Country Avg', 'Hip Hop Avg'}
          True
          >>> 0 < words.column('Country Avg').item(0) < 1
          True
          >>> 0 < words.column('Hip Hop Avg').item(0) < 1
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
