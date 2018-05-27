test = {
  'name': '2.2.1',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> classify(np.array(test_20.row(0)), train_20, train_lyrics.column('Genre'), 5) in ['Country', 'Hip-hop']
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
