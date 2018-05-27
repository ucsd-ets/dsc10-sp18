test = {
  'name': '3.0.1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> word_average(country_words).num_rows == country_words.num_columns
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
