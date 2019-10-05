from kubernetes import client, config
import glob

config.load_kube_config()
namespace = "kbit-devops"
cm_name = "kbit-test-reports"


# def create_cm_with_report(cm_name, report_name, report_context, ):
#     api_instance = client.CoreV1Api()
#     body = client.V1ConfigMap()
#     metadata = client.V1ObjectMeta(name=cm_name)
#     body.metadata = metadata
#     body.data = {report_name: report_context}
#     api_instance.create_namespaced_config_map(namespace, body)


def add_report_to_cm(reports):
    data = {}
    api_instance = client.CoreV1Api()
    body = client.V1ConfigMap()
    cm = api_instance.read_namespaced_config_map(cm_name, namespace)
    for report in reports:
        if cm.data is None:
            data[report['cm_key']] = report['content']
        elif report['cm_key'] not in cm.data.keys():
            data[report['cm_key']] = report['content']
    body.data = data
    api_instance.patch_namespaced_config_map(cm_name, namespace, body)


def get_report_name():
    return glob.glob("./reports/*.html")[0].split("/")[2]


def read_reports():
    reports = []
    for report in glob.glob("./reports/*.html"):
        file_name = report
        cm_key = report.split("/")[2]
        reports.append({'file_name': file_name, 'cm_key': cm_key, 'content': ""})
    for report in reports:
        with open(report['file_name'], "r") as f:
            report['content'] = f.read()
        f.close()
    return reports


def main():
    add_report_to_cm(read_reports())


if __name__ == "__main__":
    main()
