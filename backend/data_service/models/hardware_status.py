from typing import Optional

from pydantic import BaseModel, Field


class HardwareStatus(BaseModel):
    cpu_temp: int = Field(alias="cputemp")
    host_name: str = Field(alias="hostname")
    IPv4: str
    free_heap_memory: str = Field(alias="freeHeapMem")
    firmware: Optional[str]
    build_time: Optional[str] = Field(alias="buildtime")
    git_branch: Optional[str] = Field(alias="gitbranch")
    git_tag: Optional[str] = Field(alias="gittag")
    git_revision: Optional[str] = Field(alias="gitrevision")
    html: Optional[str]
