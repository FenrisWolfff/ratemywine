create table main.app_country
(
    id           integer     not null
        primary key autoincrement,
    name         varchar(50) not null
        unique,
    abbreviation varchar(4)  not null
);

create table main.app_region
(
    id              integer     not null
        primary key autoincrement,
    name            varchar(50) not null,
    country_id      bigint      not null
        references main.app_country
            deferrable initially deferred,
    parentRegion_id bigint
        references main.app_region
            deferrable initially deferred
);

create table main.app_appellation
(
    id        integer     not null
        primary key autoincrement,
    name      varchar(50) not null,
    region_id bigint      not null
        references main.app_region
            deferrable initially deferred
);

create index main.app_appellation_region_id_cafc4a94
    on main.app_appellation (region_id);

create index main.app_region_country_id_900cefa3
    on main.app_region (country_id);

create index main.app_region_parentRegion_id_9694e4bd
    on main.app_region (parentRegion_id);

create table main.app_varietal
(
    id   integer     not null
        primary key autoincrement,
    name varchar(50) not null
);

create table main.app_winery
(
    id   integer     not null
        primary key autoincrement,
    name varchar(50) not null
);

create table main.app_wine
(
    id             integer     not null
        primary key autoincrement,
    designation    varchar(50),
    wineType       varchar(10) not null,
    vineyard       varchar(50) not null,
    appellation_id bigint      not null
        references main.app_appellation
            deferrable initially deferred,
    varietal_id    bigint      not null
        references main.app_varietal
            deferrable initially deferred,
    winery_id      bigint      not null
        references main.app_winery
            deferrable initially deferred,
    picture        varchar(100)
);

create index main.app_wine_appellation_id_a0d56494
    on main.app_wine (appellation_id);

create index main.app_wine_varietal_id_647b82af
    on main.app_wine (varietal_id);

create index main.app_wine_winery_id_7f6fc49a
    on main.app_wine (winery_id);

create table main.auth_group
(
    id   integer      not null
        primary key autoincrement,
    name varchar(150) not null
        unique
);

create table main.auth_user
(
    id           integer      not null
        primary key autoincrement,
    password     varchar(128) not null,
    last_login   datetime,
    is_superuser bool         not null,
    username     varchar(150) not null
        unique,
    last_name    varchar(150) not null,
    email        varchar(254) not null,
    is_staff     bool         not null,
    is_active    bool         not null,
    date_joined  datetime     not null,
    first_name   varchar(150) not null
);

create table main.app_rating
(
    id        integer           not null
        primary key autoincrement,
    vintage   smallint unsigned not null,
    timestamp datetime          not null,
    rating    smallint unsigned not null,
    tannin    smallint unsigned not null,
    sweetness smallint unsigned not null,
    alcohol   smallint unsigned not null,
    acidity   smallint unsigned not null,
    body      smallint unsigned not null,
    finish    smallint unsigned not null,
    price     real              not null,
    comment   text,
    wine_id   bigint            not null
        references main.app_wine
            deferrable initially deferred,
    user_id   integer           not null
        references main.auth_user
            deferrable initially deferred,
    check ("acidity" >= 0),
    check ("alcohol" >= 0),
    check ("body" >= 0),
    check ("finish" >= 0),
    check ("rating" >= 0),
    check ("sweetness" >= 0),
    check ("tannin" >= 0),
    check ("vintage" >= 0)
);

create index main.app_rating_user_id_3d95154b
    on main.app_rating (user_id);

create index main.app_rating_wine_id_1ccfb2d8
    on main.app_rating (wine_id);

create table main.auth_user_groups
(
    id       integer not null
        primary key autoincrement,
    user_id  integer not null
        references main.auth_user
            deferrable initially deferred,
    group_id integer not null
        references main.auth_group
            deferrable initially deferred
);

create index main.auth_user_groups_group_id_97559544
    on main.auth_user_groups (group_id);

create index main.auth_user_groups_user_id_6a12ed8b
    on main.auth_user_groups (user_id);

create unique index main.auth_user_groups_user_id_group_id_94350c0c_uniq
    on main.auth_user_groups (user_id, group_id);

create table main.django_content_type
(
    id        integer      not null
        primary key autoincrement,
    app_label varchar(100) not null,
    model     varchar(100) not null
);

create table main.auth_permission
(
    id              integer      not null
        primary key autoincrement,
    content_type_id integer      not null
        references main.django_content_type
            deferrable initially deferred,
    codename        varchar(100) not null,
    name            varchar(255) not null
);

create table main.auth_group_permissions
(
    id            integer not null
        primary key autoincrement,
    group_id      integer not null
        references main.auth_group
            deferrable initially deferred,
    permission_id integer not null
        references main.auth_permission
            deferrable initially deferred
);

create index main.auth_group_permissions_group_id_b120cbf9
    on main.auth_group_permissions (group_id);

create unique index main.auth_group_permissions_group_id_permission_id_0cd325b0_uniq
    on main.auth_group_permissions (group_id, permission_id);

create index main.auth_group_permissions_permission_id_84c5c92e
    on main.auth_group_permissions (permission_id);

create index main.auth_permission_content_type_id_2f476e4b
    on main.auth_permission (content_type_id);

create unique index main.auth_permission_content_type_id_codename_01ab375a_uniq
    on main.auth_permission (content_type_id, codename);

create table main.auth_user_user_permissions
(
    id            integer not null
        primary key autoincrement,
    user_id       integer not null
        references main.auth_user
            deferrable initially deferred,
    permission_id integer not null
        references main.auth_permission
            deferrable initially deferred
);

create index main.auth_user_user_permissions_permission_id_1fbb5f2c
    on main.auth_user_user_permissions (permission_id);

create index main.auth_user_user_permissions_user_id_a95ead1b
    on main.auth_user_user_permissions (user_id);

create unique index main.auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
    on main.auth_user_user_permissions (user_id, permission_id);

create table main.django_admin_log
(
    id              integer           not null
        primary key autoincrement,
    object_id       text,
    object_repr     varchar(200)      not null,
    action_flag     smallint unsigned not null,
    change_message  text              not null,
    content_type_id integer
        references main.django_content_type
            deferrable initially deferred,
    user_id         integer           not null
        references main.auth_user
            deferrable initially deferred,
    action_time     datetime          not null,
    check ("action_flag" >= 0)
);

create index main.django_admin_log_content_type_id_c4bce8eb
    on main.django_admin_log (content_type_id);

create index main.django_admin_log_user_id_c564eba6
    on main.django_admin_log (user_id);

create unique index main.django_content_type_app_label_model_76bd3d3b_uniq
    on main.django_content_type (app_label, model);

create table main.django_migrations
(
    id      integer      not null
        primary key autoincrement,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime     not null
);

create table main.django_session
(
    session_key  varchar(40) not null
        primary key,
    session_data text        not null,
    expire_date  datetime    not null
);

create index main.django_session_expire_date_a5c62663
    on main.django_session (expire_date);

create table main.sqlite_master
(
    type     TEXT,
    name     TEXT,
    tbl_name TEXT,
    rootpage INT,
    sql      TEXT
);

create table main.sqlite_sequence
(
    name,
    seq
);

