test = {
  'name': '3.1.1',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < solo_accuracies.index_by('Feature').get('heart')[0][1] < 1
          True
          >>> solo_accuracies.labels == ('Feature', 'Solo Accuracy')
          True
          >>> np.allclose(solo_accuracies.sort(1, descending=True).column(1), solo_accuracies.column(1))
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
