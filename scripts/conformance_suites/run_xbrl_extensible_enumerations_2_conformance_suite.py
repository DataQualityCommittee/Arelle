import os

from arelle.CntlrCmdLine import parseAndRun

# from https://specifications.xbrl.org/work-product-index-extensible-enumerations-extensible-enumerations-2.0.html
CONFORMANCE_SUITE = 'tests/resources/conformance_suites/extensible-enumerations-2.0-2020-02-12.zip/extensible-enumerations-2.0-2020-02-12'
ARGS = [
    '--csvTestReport', 'extensible-enumerations-2-report.csv',
    '--file', os.path.join(CONFORMANCE_SUITE, 'enumerations-index.xml'),
    '--logFile', 'extensible-enumerations-2-log.txt',
    '--testcaseResultsCaptureWarnings',
    '--validate',
]


def run_xbrl_extensible_enumerations_2_conformance_suite(args):
    """
    Kicks off the validation of the XBRL Extensible Enumerations 2.0 conformance suite.

    :param args: The arguments to pass to Arelle in order to accurately validate the XBRL Extensible Enumerations 2.0 conformance suite
    :param args: list of str
    :return: Returns the result of parseAndRun which in this case is the created controller object
    :rtype: ::class:: `~arelle.CntlrCmdLine.CntlrCmdLine`
    """
    return parseAndRun(args)


if __name__ == "__main__":
    print('Running XBRL Extensible Enumerations 2.0 tests...')
    run_xbrl_extensible_enumerations_2_conformance_suite(ARGS)
