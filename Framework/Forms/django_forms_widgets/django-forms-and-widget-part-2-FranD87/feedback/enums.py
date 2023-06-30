class SectionChoices:

    def __get__(self, obj, type=None) -> object:
        return (
            ("ComputerRelated", "ComputerRelated"),
            ("PlatformRelated", "PlatformRelated"),
            ("InternetRelated", "InternetRelated"),
            ("userRelated", "userRelated"),
        )

    def __set__(self, obj, value) -> None:
        raise AttributeError("cannot set constant value")


class Gender:

    def __get__(self, obj, type=None) -> object:
        return (
            ("Male", "Male"),
            ("Female", "Female"),
        )

    def __set__(self, obj, value) -> None:
        raise AttributeError("cannot set constant value")


class Constants:
    SECTION_CHOICES = SectionChoices()
    GENDER_CHOICES = Gender()