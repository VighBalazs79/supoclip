from __future__ import annotations

from typing import Optional

from ..config import Config
from ..models import User
from .email_service import EmailContent, ResendEmailService, first_name_for


class SubscriptionEmailService:
    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self.email_service = ResendEmailService(self.config)

    @property
    def is_configured(self) -> bool:
        return self.email_service.is_configured

    async def send_subscribed_email(self, user: User) -> dict:
        content = self._build_subscribed_email(user)
        return await self.email_service.send_email(user.email, content)

    async def send_unsubscribed_email(self, user: User) -> dict:
        content = self._build_unsubscribed_email(user)
        return await self.email_service.send_email(user.email, content)

    def _build_subscribed_email(self, user: User) -> EmailContent:
        first_name = self._first_name_for(user)
        return EmailContent(
            subject="Thanks for subscribing to Zyntro",
            html=(
                f"<p>Hi {first_name},</p>"
                "<p>Thanks for subscribing to Zyntro.</p>"
                "<p>Your paid plan is now active, and you can jump back in anytime to create more clips.</p>"
                "<p>We’re excited to have you with us.</p>"
                "<p>Team Zyntro</p>"
            ),
            text=(
                f"Hi {first_name},\n\n"
                "Thanks for subscribing to Zyntro.\n\n"
                "Your paid plan is now active, and you can jump back in anytime to create more clips.\n\n"
                "We’re excited to have you with us.\n\n"
                "Team Zyntro"
            ),
        )

    def _build_unsubscribed_email(self, user: User) -> EmailContent:
        first_name = self._first_name_for(user)
        return EmailContent(
            subject="Sorry to see you go from Zyntro",
            html=(
                f"<p>Hi {first_name},</p>"
                "<p>Sorry to see you go, and thanks for trying Zyntro.</p>"
                "<p>Your subscription has been canceled. If you ever want to come back, we’d love to have you.</p>"
                "<p>Team Zyntro</p>"
            ),
            text=(
                f"Hi {first_name},\n\n"
                "Sorry to see you go, and thanks for trying Zyntro.\n\n"
                "Your subscription has been canceled. If you ever want to come back, we’d love to have you.\n\n"
                "Team Zyntro"
            ),
        )

    @staticmethod
    def _first_name_for(user: User) -> str:
        return first_name_for(first_name=user.first_name, full_name=user.name)
