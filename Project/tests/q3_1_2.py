test = {
  'name': '3.1.2',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 0 < ablation_accuracies.index_by('Feature').get('heart')[0][1] < 1
          True
          >>> np.allisclose(ablation_accuracies.sort(1, descending=True).column(1), ablation_accuracies.column(1))
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
