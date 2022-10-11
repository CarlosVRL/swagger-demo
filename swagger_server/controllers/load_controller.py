import connexion
import six

from swagger_server.models.load_list import LoadList  # noqa: E501
from swagger_server.models.parameter_list import ParameterList  # noqa: E501
from swagger_server import util


def get_loads_from_parameters(body):  # noqa: E501
    """Convert Parameter Inputs to Load Outputs

    Transform Parameter Data to Loads Data # noqa: E501

    :param body: Optional description in *Markdown*
    :type body: dict | bytes

    :rtype: LoadList
    """
    
    # parse parameter inputs
    if connexion.request.is_json:
        body = ParameterList.from_dict(connexion.request.get_json())  # noqa: E501
    
    # convert to loads (lookup-table, equation-based, system process, etc.)

    # mock load algorithm: load[i] = 2 * parameter[i]
    loads = LoadList(
        2.0 * body.param1, 
        2.0 * body.param2, 
        2.0 * body.param3)
    return loads
