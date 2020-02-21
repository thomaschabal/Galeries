from sqlalchemy import desc, between

from .ResourceDAO import ResourceDAO
from ..services import UserService
from ..models import Gallery, Year, Event, User


class GalleryDAO(ResourceDAO):
    def __init__(self):
        super().__init__(Gallery)
    
    @staticmethod
    def has_basic_user_right_on(gallery, current_user: User):
        first_allowed_year, last_allowed_year = UserService.get_user_allowed_years(current_user.promotion)
        gallery_year = gallery.year.value
        if gallery_year >= first_allowed_year and gallery_year <= last_allowed_year:
            return True
        return False


    @staticmethod
    def find_by_event_and_year_slugs(event_slug: str,  year_slug: str):
        return Gallery.query.join(Gallery.year).join(Gallery.event).filter(Year.slug == year_slug, Event.slug == event_slug).all()

    @staticmethod
    def find_public_by_year(year: Year):
        return Gallery.query.filter_by(year=year, private=False).all()

    @classmethod
    def find_private_by_year(cls, year: Year, current_user: User):
        galleries = Gallery.query.filter_by(year=year, private=True).all()
        return list(filter(lambda gallery: cls.has_right_on(gallery, current_user), galleries))

    @staticmethod
    def find_public():
        return Gallery.query.filter_by(private=False).all()

    @staticmethod
    def find_private():
        return Gallery.query.filter_by(private=True).all()

    @staticmethod
    def all_public_sorted_by_date():
        return Gallery.query.filter_by(private=False).order_by(desc(Gallery.created))

    @staticmethod
    def find_all_public_sorted_by_date():
        return GalleryDAO.all_public_sorted_by_date().all()
    
    @staticmethod
    def count_all_public_sorted_by_date():
        return GalleryDAO.all_public_sorted_by_date().count()

    @staticmethod
    def find_public_sorted_by_date(page=None, page_size=None):
        if page_size is None:
            return GalleryDAO.find_all_public_sorted_by_date()
        else:
            if page is None:
                page = 1
            return Gallery.query.filter_by(private=False).order_by(desc(Gallery.created)).offset(
                (page - 1) * page_size).limit(page_size).all()

    # Add a filter by years on find_public_sorted_by_date methods
    @staticmethod
    def all_public_sorted_by_date_filtered_by_years(beginning_year, ending_year):
        return Gallery.query.join(Gallery.year).filter(Gallery.private == False).filter(Year.slug >= beginning_year, Year.slug <= ending_year).order_by(desc(Gallery.created))

    @staticmethod
    def find_all_public_sorted_by_date_filtered_by_years(beginning_year, ending_year):
        return GalleryDAO.all_public_sorted_by_date_filtered_by_years(beginning_year, ending_year).all()
    
    @staticmethod
    def count_all_public_sorted_by_date_filtered_by_years(beginning_year, ending_year):
        return GalleryDAO.all_public_sorted_by_date_filtered_by_years(beginning_year, ending_year).count()

    @staticmethod
    def find_public_sorted_by_date_filtered_by_years(beginning_year, ending_year, page=None, page_size=None):
        if page_size is None:
            return GalleryDAO.find_all_public_sorted_by_date_filtered_by_years(beginning_year, ending_year)
        else:
            if page is None:
                page = 1
            return Gallery.query.join(Gallery.year).filter(Gallery.private == False).filter(Year.slug >= beginning_year, Year.slug <= ending_year).order_by(desc(Gallery.created)).offset((page-1)*page_size).limit(page_size).all()