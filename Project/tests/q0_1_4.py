test = {
  'name': '0.1.4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> row = vocab_table.where('Word', most_shortened).row(0)
          >>> len(row.item('Word')) > len(row.item('Stem'))
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
