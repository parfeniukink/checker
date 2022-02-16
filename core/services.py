import asyncio
from datetime import datetime
from typing import Optional

from httpx import AsyncClient

from core.models import Report, ReportStatuses, Website


class Checker:
    async def get_report_by_website(self, website, time: datetime):
        # async with AsyncClient(timeout=Timeout(5, read=None)) as client:
        async with AsyncClient() as client:
            try:
                result = await client.get(website.url, follow_redirects=True)
                if result.status_code < 300:
                    return Report(
                        site=website,
                        status=ReportStatuses.AVAILABLE.value,
                        created_at=time,
                    )
                elif result.status_code < 500:
                    return Report(
                        site=website,
                        status=ReportStatuses.BLOCKED.value,
                        created_at=time,
                    )
                elif result.status_code >= 500:
                    return Report(
                        site=website,
                        status=ReportStatuses.NOT_AVAILABLE.value,
                        created_at=time,
                    )
            except Exception:
                print(">>> Somthing wrong...")

    @property
    def websites(self):
        return Website.objects.all()

    def save_to_db(self, reports: list[Report]) -> list[Report]:
        objects = Report.objects.bulk_create(reports)
        return objects

    def generate_reports(self):
        now = datetime.now()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop = asyncio.get_event_loop()
        tasks = [
            self.get_report_by_website(website=site, time=now) for site in self.websites
        ]
        reports: tuple[Optional[Report]] = loop.run_until_complete(
            asyncio.gather(*tasks)
        )
        loop.close()

        self.save_to_db(reports=[r for r in reports if r])
        return reports
