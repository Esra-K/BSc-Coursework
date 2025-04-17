from django.test import SimpleTestCase
from shabook.forms import PictureUpdateForm

class TestForms(SimpleTestCase):

    def test_PictureUpdateForm_from_valid_data(self):
        form = PictureUpdateForm(data = {
            'title' : 'War and Peace' ,
            'edition' : 5 ,
            'book_author' : 'Leo tolstoy' ,
            'publications' : 'The Russiasn Messenger'
        })

        #self.assertTrue(form.is_valid())

    def test_PictureUpdateForm_from_no_data(self):
        form = PictureUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors) , 4)
