import _plotly_utils.basevalidators


class ScalemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='scalemode', parent_name='violin', **kwargs
    ):
        super(ScalemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            values=['width', 'count'],
            **kwargs
        )