import os
import sys

import xlrd
from .models import Patient, Questionnaire


class UploadingPatient(object):
    foreign_key_fields = {""}
    model = Patient

    def __init__(self, data):
        data = data
        self.uploaded_file = data.get("file")
        self.parsing()

    def getting_related_model(self, field_name):
        related_model = self.model._meta.get_field(field_name).remote_field.model if \
            self.model._meta.get_field(field_name).remote_field else \
            self.model._meta.get_field(field_name).rel.to
        return related_model

    def getting_headers(self):
        s = self.s
        headers = dict()
        for column in range(s.ncols):
            value = s.cell(0,column).value
            headers[column]=value
        return headers

    def parsing(self):
        uploaded_file = self.uploaded_file
        wb = xlrd.open_workbook(file_contents=uploaded_file.read(), encoding_override="utf-8")
        s = wb.sheet_by_index(0)
        self.s = s

        headers = self.getting_headers()

        patient_bulk_list = list()
        for row in range(1,s.nrows):
            row_dict = {}
            for column in range(s.ncols):
                value = s.cell(row,column).value
                field_name = headers[column]

                if field_name == "id" and not value:
                    continue
                if field_name in self.foreign_key_fields:
                    related_model = self.getting_related_model(field_name)
                    instance, created = related_model.objects.get_or_create(name = value)
                    value = instance
                row_dict[field_name] = value
                #patient_bulk_list.append(Patient(**row_dict))
            Patient.objects.create(**row_dict)
        #Patient.objects.bulk_create(patient_bulk_list)
        return True


class UploadingQuestionnaire(object):
    foreign_key_fields = {"patient"}
    model = Questionnaire

    def __init__(self, data):
        data = data
        self.uploaded_file = data.get("file")
        self.parsing()

    def getting_related_model(self, field_name):
        related_model = self.model._meta.get_field(field_name).remote_field.model if \
            self.model._meta.get_field(field_name).remote_field else \
            self.model._meta.get_field(field_name).rel.to
        return related_model

    def getting_headers(self):
        s = self.s
        headers = dict()
        for column in range(s.ncols):
            value = s.cell(0,column).value
            headers[column]=value
        return headers

    def parsing(self):
        uploaded_file = self.uploaded_file
        wb = xlrd.open_workbook(file_contents=uploaded_file.read())
        s = wb.sheet_by_index(0)
        self.s = s

        headers = self.getting_headers()

        patient_bulk_list = list()
        for row in range(1,s.nrows):
            row_dict = {}
            for column in range(s.ncols):
                value = s.cell(row,column).value
                field_name = headers[column]

                if field_name == "id" and not value:
                    continue
                if field_name in self.foreign_key_fields:
                    related_model = self.getting_related_model(field_name)
                    instance, created = related_model.objects.get_or_create(fullname = value)
                    value = instance
                row_dict[field_name] = value
                #patient_bulk_list.append(Questionnaire(**row_dict))
            Questionnaire.objects.create(**row_dict)
        #Questionnaire.objects.bulk_create(patient_bulk_list)
        return True
