from sklearn.base import TransformerMixin

class Preprocessor(TransformerMixin):
    def fit_transform(self, X, y=None, **fit_params):
        return super().fit_transform(X, y, **fit_params)
