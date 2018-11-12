from .entity import Entity
from .service import Service


class EscalationPolicy(Entity):
    """PagerDuty event rule entity."""

    STR_OUTPUT_FIELDS = ('id',)

    def services(self):
        """Fetch all instances of services for this ER."""
        ids = [x[1] for x in self['actions'] if x[0] == 'route']
        return [Service.fetch(id) for id in ids]
