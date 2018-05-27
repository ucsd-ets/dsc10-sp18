test = {
  'name': '3.0.3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.all([f in test_lyrics.labels for f in most_country])
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
