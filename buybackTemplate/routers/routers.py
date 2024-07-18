
class SDERouter:
    """Router for the SDE database"""
    route_app_labels = {'sde'}

    def db_for_read(self, model, **hints):
        """Reads from sde"""
        if model._meta.app_label in self.route_app_labels:
            return 'sde'
        return None

    def db_for_write(self, model, **hints):
        """Writes to sde"""
        if model._meta.app_label in self.route_app_labels:
            return 'sde'
        return None

    def allow_relations(self, obj1, obj2, **hints):
        """Relations for sde"""
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Allows migrates for sde"""
        if app_label in self.route_app_labels:
            return db == 'sde'
        return None
